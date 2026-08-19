# SyndProxy private pool

## Current pool

- Alive now: 913
- Gold now: 354
- HTTP: 272 alive / 73 gold
- HTTPS: 208 alive / 13 gold
- SOCKS4: 209 alive / 123 gold
- SOCKS5: 224 alive / 145 gold

## Historical pool

- Discovered: 129290
- Ever alive: 20291
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
