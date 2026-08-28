# SyndProxy validated proxy pool

## Current pool

- Alive now: 580
- Gold now: 429
- HTTP: 108 alive / 79 gold
- HTTPS: 114 alive / 19 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 187 alive / 172 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42462
- Ever gold: 1357

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
