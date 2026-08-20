# SyndProxy private pool

## Current pool

- Alive now: 873
- Gold now: 353
- HTTP: 265 alive / 76 gold
- HTTPS: 213 alive / 17 gold
- SOCKS4: 202 alive / 132 gold
- SOCKS5: 193 alive / 128 gold

## Historical pool

- Discovered: 149491
- Ever alive: 26565
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
