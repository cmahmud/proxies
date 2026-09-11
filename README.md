# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 419
- HTTP: 95 alive / 67 gold
- HTTPS: 41 alive / 18 gold
- SOCKS4: 181 alive / 164 gold
- SOCKS5: 193 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48952
- Ever gold: 1569

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
