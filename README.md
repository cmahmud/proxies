# SyndProxy private pool

## Current pool

- Alive now: 765
- Gold now: 398
- HTTP: 175 alive / 88 gold
- HTTPS: 135 alive / 21 gold
- SOCKS4: 227 alive / 138 gold
- SOCKS5: 228 alive / 151 gold

## Historical pool

- Discovered: 154732
- Ever alive: 29180
- Ever gold: 1124

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
