# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 390
- HTTP: 107 alive / 61 gold
- HTTPS: 45 alive / 9 gold
- SOCKS4: 169 alive / 157 gold
- SOCKS5: 186 alive / 163 gold

## Historical pool

- Discovered: 177586
- Ever alive: 33321
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
