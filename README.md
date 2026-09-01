# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 443
- HTTP: 92 alive / 71 gold
- HTTPS: 109 alive / 32 gold
- SOCKS4: 171 alive / 163 gold
- SOCKS5: 189 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47406
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
