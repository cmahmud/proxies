# SyndProxy private pool

## Current pool

- Alive now: 1641
- Gold now: 647
- HTTP: 660 alive / 242 gold
- HTTPS: 518 alive / 129 gold
- SOCKS4: 216 alive / 133 gold
- SOCKS5: 247 alive / 143 gold

## Historical pool

- Discovered: 142727
- Ever alive: 24535
- Ever gold: 1027

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
