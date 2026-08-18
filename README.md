# SyndProxy private pool

## Current pool

- Alive now: 633
- Gold now: 221
- HTTP: 181 alive / 29 gold
- HTTPS: 77 alive / 8 gold
- SOCKS4: 192 alive / 106 gold
- SOCKS5: 183 alive / 78 gold

## Historical pool

- Discovered: 86697
- Ever alive: 6452
- Ever gold: 300

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
