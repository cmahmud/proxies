# SyndProxy validated proxy pool

## Current pool

- Alive now: 613
- Gold now: 459
- HTTP: 127 alive / 86 gold
- HTTPS: 128 alive / 35 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 185 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46706
- Ever gold: 1446

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
