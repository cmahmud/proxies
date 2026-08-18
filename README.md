# SyndProxy private pool

## Current pool

- Alive now: 826
- Gold now: 238
- HTTP: 254 alive / 31 gold
- HTTPS: 128 alive / 8 gold
- SOCKS4: 252 alive / 134 gold
- SOCKS5: 192 alive / 65 gold

## Historical pool

- Discovered: 94344
- Ever alive: 9662
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
