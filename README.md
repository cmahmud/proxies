# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 390
- HTTP: 123 alive / 64 gold
- HTTPS: 52 alive / 9 gold
- SOCKS4: 171 alive / 157 gold
- SOCKS5: 187 alive / 160 gold

## Historical pool

- Discovered: 177586
- Ever alive: 33322
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
