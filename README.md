# SyndProxy private pool

## Current pool

- Alive now: 711
- Gold now: 391
- HTTP: 154 alive / 82 gold
- HTTPS: 123 alive / 19 gold
- SOCKS4: 220 alive / 146 gold
- SOCKS5: 214 alive / 144 gold

## Historical pool

- Discovered: 144748
- Ever alive: 25212
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
