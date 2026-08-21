# SyndProxy private pool

## Current pool

- Alive now: 1074
- Gold now: 368
- HTTP: 398 alive / 95 gold
- HTTPS: 265 alive / 21 gold
- SOCKS4: 186 alive / 116 gold
- SOCKS5: 225 alive / 136 gold

## Historical pool

- Discovered: 153747
- Ever alive: 28816
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
