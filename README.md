# SyndProxy validated proxy pool

## Current pool

- Alive now: 646
- Gold now: 472
- HTTP: 136 alive / 93 gold
- HTTPS: 130 alive / 43 gold
- SOCKS4: 181 alive / 163 gold
- SOCKS5: 199 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46959
- Ever gold: 1461

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
