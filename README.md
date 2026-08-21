# SyndProxy private pool

## Current pool

- Alive now: 879
- Gold now: 402
- HTTP: 274 alive / 87 gold
- HTTPS: 158 alive / 26 gold
- SOCKS4: 220 alive / 142 gold
- SOCKS5: 227 alive / 147 gold

## Historical pool

- Discovered: 157420
- Ever alive: 29724
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
