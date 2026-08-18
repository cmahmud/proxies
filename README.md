# SyndProxy private pool

## Current pool

- Alive now: 1032
- Gold now: 233
- HTTP: 362 alive / 23 gold
- HTTPS: 175 alive / 8 gold
- SOCKS4: 275 alive / 116 gold
- SOCKS5: 220 alive / 86 gold

## Historical pool

- Discovered: 86712
- Ever alive: 6879
- Ever gold: 320

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
