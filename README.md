# SyndProxy private pool

## Current pool

- Alive now: 929
- Gold now: 409
- HTTP: 268 alive / 79 gold
- HTTPS: 205 alive / 28 gold
- SOCKS4: 214 alive / 155 gold
- SOCKS5: 242 alive / 147 gold

## Historical pool

- Discovered: 165846
- Ever alive: 32373
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
