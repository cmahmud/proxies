# SyndProxy validated proxy pool

## Current pool

- Alive now: 378
- Gold now: 299
- HTTP: 83 alive / 56 gold
- HTTPS: 33 alive / 11 gold
- SOCKS4: 115 alive / 107 gold
- SOCKS5: 147 alive / 125 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49487
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
