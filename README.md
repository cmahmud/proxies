# SyndProxy validated proxy pool

## Current pool

- Alive now: 454
- Gold now: 373
- HTTP: 88 alive / 59 gold
- HTTPS: 33 alive / 9 gold
- SOCKS4: 159 alive / 151 gold
- SOCKS5: 174 alive / 154 gold

## Historical pool

- Discovered: 174307
- Ever alive: 33082
- Ever gold: 1225

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
