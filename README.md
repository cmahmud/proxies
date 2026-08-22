# SyndProxy private pool

## Current pool

- Alive now: 793
- Gold now: 380
- HTTP: 242 alive / 86 gold
- HTTPS: 135 alive / 21 gold
- SOCKS4: 195 alive / 126 gold
- SOCKS5: 221 alive / 147 gold

## Historical pool

- Discovered: 162003
- Ever alive: 31390
- Ever gold: 1159

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
