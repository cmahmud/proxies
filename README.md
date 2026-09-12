# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 468
- HTTP: 125 alive / 94 gold
- HTTPS: 63 alive / 37 gold
- SOCKS4: 183 alive / 161 gold
- SOCKS5: 190 alive / 176 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49378
- Ever gold: 1579

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
