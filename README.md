# SyndProxy private pool

## Current pool

- Alive now: 891
- Gold now: 412
- HTTP: 280 alive / 82 gold
- HTTPS: 173 alive / 26 gold
- SOCKS4: 184 alive / 133 gold
- SOCKS5: 254 alive / 171 gold

## Historical pool

- Discovered: 162742
- Ever alive: 31476
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
