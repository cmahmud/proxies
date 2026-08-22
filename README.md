# SyndProxy private pool

## Current pool

- Alive now: 873
- Gold now: 404
- HTTP: 254 alive / 89 gold
- HTTPS: 181 alive / 27 gold
- SOCKS4: 216 alive / 145 gold
- SOCKS5: 222 alive / 143 gold

## Historical pool

- Discovered: 163255
- Ever alive: 31765
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
