# SyndProxy private pool

## Current pool

- Alive now: 1353
- Gold now: 543
- HTTP: 519 alive / 187 gold
- HTTPS: 350 alive / 54 gold
- SOCKS4: 231 alive / 145 gold
- SOCKS5: 253 alive / 157 gold

## Historical pool

- Discovered: 125594
- Ever alive: 19575
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
