# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 407
- HTTP: 110 alive / 62 gold
- HTTPS: 68 alive / 17 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 185 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38378
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
