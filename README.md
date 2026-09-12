# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 456
- HTTP: 127 alive / 90 gold
- HTTPS: 61 alive / 31 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 187 alive / 174 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49374
- Ever gold: 1579

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
