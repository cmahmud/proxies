# SyndProxy private pool

## Current pool

- Alive now: 876
- Gold now: 372
- HTTP: 272 alive / 92 gold
- HTTPS: 194 alive / 15 gold
- SOCKS4: 219 alive / 142 gold
- SOCKS5: 191 alive / 123 gold

## Historical pool

- Discovered: 119831
- Ever alive: 18266
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
