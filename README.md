# SyndProxy validated proxy pool

## Current pool

- Alive now: 585
- Gold now: 421
- HTTP: 104 alive / 75 gold
- HTTPS: 124 alive / 17 gold
- SOCKS4: 165 alive / 161 gold
- SOCKS5: 192 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42479
- Ever gold: 1357

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
