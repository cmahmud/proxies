# SyndProxy private pool

## Current pool

- Alive now: 982
- Gold now: 387
- HTTP: 306 alive / 77 gold
- HTTPS: 212 alive / 27 gold
- SOCKS4: 212 alive / 120 gold
- SOCKS5: 252 alive / 163 gold

## Historical pool

- Discovered: 164963
- Ever alive: 32242
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
