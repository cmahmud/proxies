# SyndProxy validated proxy pool

## Current pool

- Alive now: 619
- Gold now: 466
- HTTP: 142 alive / 93 gold
- HTTPS: 118 alive / 39 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 187 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46907
- Ever gold: 1457

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
