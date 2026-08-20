# SyndProxy private pool

## Current pool

- Alive now: 1183
- Gold now: 567
- HTTP: 424 alive / 192 gold
- HTTPS: 299 alive / 95 gold
- SOCKS4: 244 alive / 146 gold
- SOCKS5: 216 alive / 134 gold

## Historical pool

- Discovered: 136255
- Ever alive: 22875
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
