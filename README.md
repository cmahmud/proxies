# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 393
- HTTP: 91 alive / 59 gold
- HTTPS: 43 alive / 9 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 192 alive / 166 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33354
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
