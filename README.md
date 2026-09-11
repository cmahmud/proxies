# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 420
- HTTP: 99 alive / 73 gold
- HTTPS: 33 alive / 13 gold
- SOCKS4: 184 alive / 164 gold
- SOCKS5: 193 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48937
- Ever gold: 1569

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
