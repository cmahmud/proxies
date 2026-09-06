# SyndProxy validated proxy pool

## Current pool

- Alive now: 434
- Gold now: 337
- HTTP: 85 alive / 60 gold
- HTTPS: 32 alive / 11 gold
- SOCKS4: 153 alive / 135 gold
- SOCKS5: 164 alive / 131 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48393
- Ever gold: 1531

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
