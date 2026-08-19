# SyndProxy private pool

## Current pool

- Alive now: 1240
- Gold now: 414
- HTTP: 427 alive / 83 gold
- HTTPS: 271 alive / 17 gold
- SOCKS4: 274 alive / 150 gold
- SOCKS5: 268 alive / 164 gold

## Historical pool

- Discovered: 131116
- Ever alive: 20634
- Ever gold: 871

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
