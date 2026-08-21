# SyndProxy private pool

## Current pool

- Alive now: 756
- Gold now: 396
- HTTP: 181 alive / 87 gold
- HTTPS: 126 alive / 21 gold
- SOCKS4: 220 alive / 135 gold
- SOCKS5: 229 alive / 153 gold

## Historical pool

- Discovered: 154732
- Ever alive: 29180
- Ever gold: 1124

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
