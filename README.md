# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 419
- HTTP: 94 alive / 73 gold
- HTTPS: 90 alive / 22 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 175 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41777
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
