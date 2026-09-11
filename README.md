# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 421
- HTTP: 95 alive / 67 gold
- HTTPS: 37 alive / 18 gold
- SOCKS4: 186 alive / 163 gold
- SOCKS5: 190 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48961
- Ever gold: 1569

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
