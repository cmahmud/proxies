# SyndProxy private pool

## Current pool

- Alive now: 870
- Gold now: 434
- HTTP: 246 alive / 94 gold
- HTTPS: 164 alive / 24 gold
- SOCKS4: 218 alive / 151 gold
- SOCKS5: 242 alive / 165 gold

## Historical pool

- Discovered: 162755
- Ever alive: 31573
- Ever gold: 1161

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
