# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 461
- HTTP: 119 alive / 93 gold
- HTTPS: 54 alive / 33 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 187 alive / 174 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49373
- Ever gold: 1579

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
