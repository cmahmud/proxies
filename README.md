# SyndProxy private pool

## Current pool

- Alive now: 1165
- Gold now: 453
- HTTP: 394 alive / 121 gold
- HTTPS: 289 alive / 41 gold
- SOCKS4: 225 alive / 142 gold
- SOCKS5: 257 alive / 149 gold

## Historical pool

- Discovered: 116452
- Ever alive: 17127
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
