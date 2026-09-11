# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 418
- HTTP: 96 alive / 66 gold
- HTTPS: 39 alive / 17 gold
- SOCKS4: 186 alive / 164 gold
- SOCKS5: 198 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48956
- Ever gold: 1569

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
