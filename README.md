# SyndProxy private pool

## Current pool

- Alive now: 1249
- Gold now: 596
- HTTP: 462 alive / 177 gold
- HTTPS: 336 alive / 113 gold
- SOCKS4: 222 alive / 144 gold
- SOCKS5: 229 alive / 162 gold

## Historical pool

- Discovered: 125594
- Ever alive: 19568
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
