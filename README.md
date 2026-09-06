# SyndProxy validated proxy pool

## Current pool

- Alive now: 480
- Gold now: 386
- HTTP: 102 alive / 71 gold
- HTTPS: 40 alive / 17 gold
- SOCKS4: 163 alive / 151 gold
- SOCKS5: 175 alive / 147 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48192
- Ever gold: 1522

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
