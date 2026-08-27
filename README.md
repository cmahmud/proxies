# SyndProxy validated proxy pool

## Current pool

- Alive now: 619
- Gold now: 410
- HTTP: 116 alive / 64 gold
- HTTPS: 142 alive / 19 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 187 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41361
- Ever gold: 1326

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
