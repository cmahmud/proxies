# SyndProxy private pool

## Current pool

- Alive now: 1334
- Gold now: 580
- HTTP: 452 alive / 189 gold
- HTTPS: 328 alive / 98 gold
- SOCKS4: 240 alive / 136 gold
- SOCKS5: 314 alive / 157 gold

## Historical pool

- Discovered: 138941
- Ever alive: 23208
- Ever gold: 915

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
