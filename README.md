# SyndProxy private pool

## Current pool

- Alive now: 1330
- Gold now: 539
- HTTP: 490 alive / 183 gold
- HTTPS: 357 alive / 59 gold
- SOCKS4: 230 alive / 142 gold
- SOCKS5: 253 alive / 155 gold

## Historical pool

- Discovered: 125594
- Ever alive: 19575
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
