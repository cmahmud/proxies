# SyndProxy validated proxy pool

## Current pool

- Alive now: 473
- Gold now: 396
- HTTP: 90 alive / 66 gold
- HTTPS: 36 alive / 21 gold
- SOCKS4: 154 alive / 136 gold
- SOCKS5: 193 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48771
- Ever gold: 1566

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
