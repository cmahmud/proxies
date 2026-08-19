# SyndProxy private pool

## Current pool

- Alive now: 1222
- Gold now: 596
- HTTP: 448 alive / 180 gold
- HTTPS: 323 alive / 110 gold
- SOCKS4: 225 alive / 145 gold
- SOCKS5: 226 alive / 161 gold

## Historical pool

- Discovered: 125594
- Ever alive: 19561
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
