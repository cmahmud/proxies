# SyndProxy private pool

## Current pool

- Alive now: 769
- Gold now: 331
- HTTP: 242 alive / 91 gold
- HTTPS: 164 alive / 28 gold
- SOCKS4: 142 alive / 85 gold
- SOCKS5: 221 alive / 127 gold

## Historical pool

- Discovered: 167131
- Ever alive: 32552
- Ever gold: 1188

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
