# SyndProxy private pool

## Current pool

- Alive now: 755
- Gold now: 397
- HTTP: 172 alive / 87 gold
- HTTPS: 129 alive / 21 gold
- SOCKS4: 223 alive / 138 gold
- SOCKS5: 231 alive / 151 gold

## Historical pool

- Discovered: 154732
- Ever alive: 29180
- Ever gold: 1124

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
