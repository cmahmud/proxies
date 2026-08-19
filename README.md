# SyndProxy private pool

## Current pool

- Alive now: 1323
- Gold now: 597
- HTTP: 519 alive / 181 gold
- HTTPS: 327 alive / 110 gold
- SOCKS4: 236 alive / 146 gold
- SOCKS5: 241 alive / 160 gold

## Historical pool

- Discovered: 125594
- Ever alive: 19561
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
