# SyndProxy private pool

## Current pool

- Alive now: 757
- Gold now: 399
- HTTP: 189 alive / 82 gold
- HTTPS: 161 alive / 27 gold
- SOCKS4: 205 alive / 147 gold
- SOCKS5: 202 alive / 143 gold

## Historical pool

- Discovered: 163333
- Ever alive: 31894
- Ever gold: 1169

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
